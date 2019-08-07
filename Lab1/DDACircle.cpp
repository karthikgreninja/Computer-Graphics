//C Program to draw circle using DDA algorithm
#include<stdio.h>
#include<graphics.h>
int main()
{
    int gd = DETECT, gm;
    int xc, yc, r, val, i;
    float xc1,xc2,yc1,yc2,eps,sx,sy;
    printf("Enter the coordinates of the centre : \n");
    printf("X coordinate : ");
    scanf("%d",&xc);
    printf("Y coordinate : ");
    scanf("%d",&yc);
    printf("Enter the radius of the circle : ");
    scanf("%d",&r);

    xc1=r;
    yc1=0;
    sx=xc1;
    sy=yc1;
    i=0;

    do  {
        val=pow(2,i);
        i++;
        }while(val<r);

    eps = 1/pow(2,i-1);
    initgraph(&gd, &gm, NULL);
    
    do  {
        xc2 = xc1 + yc1*eps;
        yc2 = yc1 - eps*xc2;
        putpixel(xc+xc2,yc-yc2,WHITE);
        delay(100);
        xc1=xc2;
        yc1=yc2;
        }while((yc1-sy)<eps || (sx-xc1)>eps);
    delay(10000000000);
}
