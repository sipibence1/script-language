import secret_logic

assert not secret_logic.is_numeric("asd"), "is_numeric with not numeric"
assert secret_logic.is_numeric("123"), "is_numeric with not numeric"


assert not secret_logic.is_supported_operator("%"), "is_supported_operator not supported operator"