class Sequential(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torch.nn.modules.conv.___torch_mangle_23.Conv2d
  __annotations__["1"] = __torch__.torch.nn.modules.batchnorm.___torch_mangle_22.BatchNorm2d
  def forward(self: __torch__.torch.nn.modules.container.___torch_mangle_24.Sequential,
    input: Tensor) -> Tensor:
    _0 = getattr(self, "0")
    _1 = getattr(self, "1")
    input0 = (_0).forward(input, )
    return (_1).forward(input0, )
  def __len__(self: __torch__.torch.nn.modules.container.___torch_mangle_24.Sequential) -> int:
    return 2
