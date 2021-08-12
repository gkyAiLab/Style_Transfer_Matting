class MaxPool2d(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  ceil_mode : Final[bool] = False
  kernel_size : Final[int] = 3
  stride : Final[int] = 2
  return_indices : Final[bool] = False
  padding : Final[int] = 1
  dilation : Final[int] = 1
  def forward(self: __torch__.torch.nn.modules.pooling.MaxPool2d,
    input: Tensor) -> Tensor:
    _0 = __torch__.torch.nn.functional._max_pool2d
    _1 = _0(input, [3, 3], [2, 2], [1, 1], [1, 1], False, False, )
    return _1
class AdaptiveAvgPool2d(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  output_size : Final[int] = 1
  def forward(self: __torch__.torch.nn.modules.pooling.AdaptiveAvgPool2d,
    input: Tensor) -> Tensor:
    _2 = __torch__.torch.nn.functional.adaptive_avg_pool2d
    return _2(input, [1, 1], )
