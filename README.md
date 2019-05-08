# Image-processing

## Interpolation

先順時針旋轉30度，再利用兩種插值法分別實作。
### Rotation

以原點為中心，順時針轉30度
x'=x cos⁡θ-y sin⁡θ
y'=x sin⁡θ+y cos⁡θ
反推，從新圖片找原圖的像素(逆時針轉30度)
x=x^'  cos⁡θ+y'sin⁡θ
y=-x'sin⁡θ+y'cos⁡θ
為了以圖片中心旋轉，須找到圖片中心點
ox=width÷2
oy=height÷2
因此，先將新圖像素平移以方便計算，旋轉後再平移回原位
nx=x^'-ox
ny=y^'-oy
x=nx^'  cos⁡θ+ny^'  sin⁡θ+ox
y=-nx^'  sin⁡θ+ny^'  cos⁡θ+oy
為了顯示所有旋轉後的像素點，必須放大旋轉後的圖片
新的圖片大小
nw=w cos⁡θ+h sin⁡θ
nh=w sin⁡θ+h cos⁡θ
因為我們的圖片都是正方形，因此可以簡化成
"nedge"="edge"(sin⁡θ+cos⁡θ)

算放大後的圖片像素點位移
ox=-nedge cos⁡θ-"nedge"  sin⁡θ+"width"÷2
oy=nedge sin⁡θ-"nedge"  cos⁡θ+"height"÷2
最終帶回原式，旋轉後平移
x=nx^'  cos⁡θ+ny^'  sin⁡θ+ox
y=-nx^'  sin⁡θ+ny^'  cos⁡θ+oy


### Nearest-neighbor interpolation (最近相鄰插值)


### Bilinear interpolation (線性插值法)


