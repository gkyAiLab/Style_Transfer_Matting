class Decoder(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  conv1 : __torch__.torch.nn.modules.conv.___torch_mangle_51.Conv2d
  bn1 : __torch__.torch.nn.modules.batchnorm.___torch_mangle_8.BatchNorm2d
  conv2 : __torch__.torch.nn.modules.conv.___torch_mangle_52.Conv2d
  bn2 : __torch__.torch.nn.modules.batchnorm.BatchNorm2d
  conv3 : __torch__.torch.nn.modules.conv.___torch_mangle_53.Conv2d
  bn3 : __torch__.torch.nn.modules.batchnorm.___torch_mangle_54.BatchNorm2d
  conv4 : __torch__.torch.nn.modules.conv.___torch_mangle_55.Conv2d
  relu : __torch__.torch.nn.modules.activation.ReLU
  def forward(self: __torch__.model.decoder.Decoder,
    x4: Tensor,
    x3: Tensor,
    x2: Tensor,
    x1: Tensor,
    x0: Tensor) -> Tensor:
    _0 = __torch__.torch.nn.functional.___torch_mangle_63.interpolate
    _1 = torch.slice(torch.size(x3), 2, 9223372036854775807, 1)
    x = _0(x4, _1, None, "bilinear", False, None, )
    x5 = torch.cat([x, x3], 1)
    x6 = (self.conv1).forward(x5, )
    x7 = (self.bn1).forward(x6, )
    x8 = (self.relu).forward(x7, )
    _2 = torch.slice(torch.size(x2), 2, 9223372036854775807, 1)
    x9 = _0(x8, _2, None, "bilinear", False, None, )
    x10 = torch.cat([x9, x2], 1)
    x11 = (self.conv2).forward(x10, )
    x12 = (self.bn2).forward(x11, )
    x13 = (self.relu).forward(x12, )
    _3 = torch.slice(torch.size(x1), 2, 9223372036854775807, 1)
    x14 = _0(x13, _3, None, "bilinear", False, None, )
    x15 = torch.cat([x14, x1], 1)
    x16 = (self.conv3).forward(x15, )
    x17 = (self.bn3).forward(x16, )
    x18 = (self.relu).forward(x17, )
    _4 = torch.slice(torch.size(x0), 2, 9223372036854775807, 1)
    x19 = _0(x18, _4, None, "bilinear", False, None, )
    x20 = torch.cat([x19, x0], 1)
    return (self.conv4).forward(x20, )
