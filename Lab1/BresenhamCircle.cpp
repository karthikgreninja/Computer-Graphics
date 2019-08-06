//C Program to implement Bresenham circle drawing algorithm
#include<stdio.h>
#include<graphics.h>
void circlePoints(int xc, int yc, int x, int y)
{
    putpixel(xc + x, yc + y,WHITE);
    putpixel(xc - x, yc + y,WHITE);
    putpixel(xc + x, yc - y,WHITE);
    putpixel(xc - x, yc - y,WHITE);
    putpixel(xc + y, yc + x,WHITE);
    putpixel(xc - y, yc + x,WHITE);
    putpixel(xc + y, yc - x,WHITE);
    putpixel(xc - y, yc - x,WHITE);
}
int main()
{
    int gd = DETECT, gm;
    int xc, yc, r, x, y, d;
    printf("Enter the coordinates of the centre : \n");
    printf("X coordinate : ");
    scanf("%d",&xc);
    printf("Y coordinate : ");
    scanf("%d",&yc);
    printf("Enter the radius of the circle : ");
    scanf("%d",&r);

    x = 0;
    y = r;
    d = 3 - 2*r;

    initgraph(&gd, &gm, NULL);
    circlePoints(xc, yc, x, y);
    while(y >= x)
    {
        x++;
        if(d > 0)
        {
            y--;
            d = d + 4*(x - y) + 10;
        }
        else
            d = d + 4*x + 6;
        circlePoints(xc, yc, x, y);
        delay(100);
    }
    delay(10000000000);
}