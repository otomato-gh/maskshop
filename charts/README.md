helm exercise based on https://github.com/otomato-gh/maskshop

Usage:
```shell
kubectl create ns maskshop
kns maskshop
git clone https://github.com/mondbev1/maskshop.git
cd maskshop
for COMPONENT in mongo api front; do helm upgrade $COMPONENT maskshop --install --values=$COMPONENT.yaml; done
```