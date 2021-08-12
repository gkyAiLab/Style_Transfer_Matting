class ResNetEncoder(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  inplanes : int
  dilation : int
  groups : int
  base_width : int
  conv1 : __torch__.torch.nn.modules.conv.Conv2d
  bn1 : __torch__.torch.nn.modules.batchnorm.BatchNorm2d
  relu : __torch__.torch.nn.modules.activation.ReLU
  maxpool : __torch__.torch.nn.modules.pooling.MaxPool2d
  layer1 : __torch__.torch.nn.modules.container.___torch_mangle_6.Sequential
  layer2 : __torch__.torch.nn.modules.container.___torch_mangle_18.Sequential
  layer3 : __torch__.torch.nn.modules.container.___torch_mangle_29.Sequential
  layer4 : __torch__.torch.nn.modules.container.___torch_mangle_40.Sequential
  def forward(self: __torch__.model.resnet.ResNetEncoder,
    x: Tensor) -> Tuple[Tensor, Tensor, Tensor, Tensor, Tensor]:
    x0 = (self.conv1).forward(x, )
    x1 = (self.bn1).forward(x0, )
    x2 = (self.relu).forward(x1, )
    x3 = (self.maxpool).forward(x2, )
    x4 = (self.layer1).forward(x3, )
    x5 = (self.layer2).forward(x4, )
    x6 = (self.layer3).forward(x5, )
    x7 = (self.layer4).forward(x6, )
    return (x7, x5, x4, x2, x)
