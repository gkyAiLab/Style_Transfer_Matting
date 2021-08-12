class Sequential(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torchvision.models.resnet.___torch_mangle_36.Bottleneck
  __annotations__["1"] = __torch__.torchvision.models.resnet.___torch_mangle_39.Bottleneck
  __annotations__["2"] = __torch__.torchvision.models.resnet.___torch_mangle_39.Bottleneck
  def forward(self: __torch__.torch.nn.modules.container.___torch_mangle_40.Sequential,
    input: Tensor) -> Tensor:
    _0 = getattr(self, "0")
    _1 = getattr(self, "1")
    _2 = getattr(self, "2")
    input0 = (_0).forward(input, )
    input1 = (_1).forward(input0, )
    return (_2).forward(input1, )
  def __len__(self: __torch__.torch.nn.modules.container.___torch_mangle_40.Sequential) -> int:
    return 3
