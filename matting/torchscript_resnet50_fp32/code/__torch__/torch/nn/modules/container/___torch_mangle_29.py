class Sequential(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torchvision.models.resnet.___torch_mangle_25.Bottleneck
  __annotations__["1"] = __torch__.torchvision.models.resnet.___torch_mangle_28.Bottleneck
  __annotations__["2"] = __torch__.torchvision.models.resnet.___torch_mangle_28.Bottleneck
  __annotations__["3"] = __torch__.torchvision.models.resnet.___torch_mangle_28.Bottleneck
  __annotations__["4"] = __torch__.torchvision.models.resnet.___torch_mangle_28.Bottleneck
  __annotations__["5"] = __torch__.torchvision.models.resnet.___torch_mangle_28.Bottleneck
  def forward(self: __torch__.torch.nn.modules.container.___torch_mangle_29.Sequential,
    input: Tensor) -> Tensor:
    _0 = getattr(self, "0")
    _1 = getattr(self, "1")
    _2 = getattr(self, "2")
    _3 = getattr(self, "3")
    _4 = getattr(self, "4")
    _5 = getattr(self, "5")
    input0 = (_0).forward(input, )
    input1 = (_1).forward(input0, )
    input2 = (_2).forward(input1, )
    input3 = (_3).forward(input2, )
    input4 = (_4).forward(input3, )
    return (_5).forward(input4, )
  def __len__(self: __torch__.torch.nn.modules.container.___torch_mangle_29.Sequential) -> int:
    return 6
