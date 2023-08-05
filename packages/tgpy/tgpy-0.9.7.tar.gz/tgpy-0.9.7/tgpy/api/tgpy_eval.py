from dataclasses import dataclass
from typing import Any

from telethon.tl.custom import Message

import tgpy.api
from tgpy import app
from tgpy._core.meval import _meval
from tgpy.api.parse_code import parse_code
from tgpy.utils import FILENAME_PREFIX, numid

variables: dict[str, Any] = {}
constants: dict[str, Any] = {}


@dataclass
class EvalResult:
    result: Any
    output: str


async def tgpy_eval(
    code: str,
    message: Message | None = None,
    *,
    filename: str | None = None,
) -> EvalResult:
    parsed = await parse_code(code, ignore_simple=False)
    if not parsed.is_code:
        if parsed.exc:
            raise parsed.exc
        else:
            raise ValueError('Invalid code provided')

    # noinspection PyProtectedMember
    app.ctx._init_stdout()
    kwargs = {'msg': message}
    if message:
        # noinspection PyProtectedMember
        app.ctx._set_msg(message)
    if not filename:
        if message:
            filename = f'{FILENAME_PREFIX}message/{message.chat_id}/{message.id}'
        else:
            filename = f'{FILENAME_PREFIX}eval/{numid()}'
    if parsed.uses_orig:
        if message:
            orig = await message.get_reply_message()
            kwargs['orig'] = orig
        else:
            kwargs['orig'] = None

    new_variables, result = await _meval(
        parsed,
        filename,
        tgpy.api.variables,
        **tgpy.api.constants,
        **kwargs,
    )
    if '__all__' in new_variables:
        new_variables = {
            k: v for k, v in new_variables.items() if k in new_variables['__all__']
        }
    tgpy.api.variables.update(new_variables)

    # noinspection PyProtectedMember
    return EvalResult(
        result=result,
        output=app.ctx._stdout,
    )


__all__ = ['variables', 'constants', 'EvalResult', 'tgpy_eval']
