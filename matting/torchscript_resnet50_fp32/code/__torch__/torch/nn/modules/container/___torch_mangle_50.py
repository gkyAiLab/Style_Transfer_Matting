class Sequential(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torch.nn.modules.conv.___torch_mangle_49.Conv2d
  __annotations__["1"] = __torch__.torch.nn.modules.batchnorm.___torch_mangle_3.BatchNorm2d
  __annotations__["2"] = __torch__.torch.nn.modules.activation.___torch_mangle_42.ReLU
  __annotations__["3"] = __torch__.torch.nn.modules.dropout.Dropout
  def forward(self: __torch__.torch.nn.modules.container.___torch_mangle_50.Sequential,
    input: Tensor) -> Tensor:
    _0 = getattr(self, "0")
    _1 = getattr(self, "1")
    _2 = getattr(self, "2")
    _3 = getattr(self, "3")
    input0 = (_0).forward(input, )
    input1 = (_1).forward(input0, )
    input2 = (_2).forward(input1, )
    return (_3).forward(input2, )
  def __len__(self: __torch__.torch.nn.modules.container.___torch_mangle_50.Sequential) -> int:
    return 4
