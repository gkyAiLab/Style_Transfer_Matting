class ReLU(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  inplace : Final[bool] = True
  def forward(self: __torch__.torch.nn.modules.activation.ReLU,
    input: Tensor) -> Tensor:
    _0 = __torch__.torch.nn.functional.relu(input, True, )
    return _0
