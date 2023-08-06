# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import copy
from textwrap import dedent

from taskgraph.transforms.base import TransformSequence
from taskgraph.util.schema import Schema, optionally_keyed_by, resolve_keyed_by
from taskgraph.util.templates import deep_get, substitute
from voluptuous import ALLOW_EXTRA, Required, Optional


CHUNK_SCHEMA = Schema(
    {
        # Optional, so it can be used for a subset of jobs in a kind
        Optional(
            "chunk-config",
            description=dedent(
                """
            `chunk-config` can be used to split one job into `total-chunks`
            jobs, substituting `this_chunk` and `total_chunks` into any
            fields in `substitution-fields`.
            """.lstrip()
            ),
        ): {
            Required(
                "total-chunks",
                description=dedent(
                    """
                The total number of chunks to split the job into.
                """.lstrip()
                ),
            ): int,
            Optional(
                "substitution-fields",
                description=dedent(
                    """
                A list of fields that need to have `{this_chunk}` and/or
                `{total_chunks}` replaced in them.
                """.lstrip()
                ),
            ): [str],
        }
    },
    extra=ALLOW_EXTRA,
)

transforms = TransformSequence()
transforms.add_validate(CHUNK_SCHEMA)


UNCHUNK_SCHEMA = Schema(
    {
        Optional(
            "unchunk-config",
            description=dedent(
                """
            `unchunk-config` can be used to duplicate the same block of a
            task definition `total-chunks` times. This is often useful when
            you have a dependency on an upstream job that is chunked, and
            you need to repeat the same `dependencies` and/or `fetches`
            for each upstream task.
            """.lstrip()
            ),
        ): {
            Required(
                "total-chunks",
                description=dedent(
                    """
                The total number of times to repeat the `per-upstream-fields`
                """.lstrip()
                ),
            ): int,
            Optional(
                "per-upstream-fields",
                description=dedent(
                    """
                An object containing the parts of the task definition that
                should be repeated. It must be defined relative to the root
                of the task definition. Any keys or values containing
                `{this_chunk}` or `{total_chunks}` will have those variables
                replaced for each upstream job.
                """.lstrip()
                ),
            ): object,
        }
    },
    extra=ALLOW_EXTRA,
)

unchunk = TransformSequence()
unchunk.add_validate(UNCHUNK_SCHEMA)


@transforms.add
def chunk_jobs(config, jobs):
    for job in jobs:
        chunk_config = job.pop("chunk-config", None)
        if not chunk_config:
            yield job
            continue

        total_chunks = chunk_config["total-chunks"]
        
        for this_chunk in range(1, total_chunks + 1):
            subjob = copy.deepcopy(job)
            
            subs = {
                "this_chunk": this_chunk,
                "total_chunks": total_chunks,
            }

            for field in chunk_config["substitution-fields"]:
                container, subfield = subjob, field
                while "." in subfield:
                    f, subfield = subfield.split(".", 1)
                    container = container[f]

                subcontainer = copy.deepcopy(container[subfield])
                subfield = substitute(subfield, **subs)
                container[subfield] = substitute(subcontainer, **subs)

            yield subjob


@unchunk.add
def do_unchunking(config, jobs):
    for job in jobs:
        unchunk_config = job.pop("unchunk-config", None)
        if not unchunk_config:
            yield job
            continue

        total_chunks = unchunk_config["total-chunks"]
        
        for this_chunk in range(1, total_chunks + 1):
            subs = {
                "this_chunk": this_chunk,
                "total_chunks": total_chunks,
            }

            for field, value in unchunk_config.get("per-upstream-fields", {}).items():
                if field not in job:
                    job[field] = {}

                job[field].update(substitute(copy.deepcopy(value), **subs))

        yield job
