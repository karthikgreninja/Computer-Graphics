//C program to implement DDA straight line drawing algorithm
#include<stdio.h>
#include<graphics.h>
int main()
{
    int gd = DETECT, gm;
    int x1, y1, x2, y2, dx, dy, step;
    float Xinc, Yinc, X, Y;

    printf("Coordinates of starting point : \n");
    printf("X coordinate : ");
    scanf("%d",&x1);
    printf("Y coordinate : ");
    scanf("%d",&y1);
    
    printf("Coordinates of ending point : \n");
    printf("X coordinate : ");
    scanf("%d",&x2);
    printf("Y coordinate : ");
    scanf("%d",&y2);
    
    dx = x2 - x1;
    dy = y2 - y1;

    step = abs(dx) > abs(dy) ? abs(dx) : abs(dy);
    printf("Steps : ",step);
    Xinc = dx / step;
    printf("\nXinc : ",Xinc);
    Yinc = dy / step;
    printf("\nYinc : ",Yinc);

    X = x1;
    Y = y1;
    
    initgraph(&gd,&gm,NULL);
    for(int i = 0;i <= step; i++)
    {
        putpixel(X,Y,WHITE);
        X += Xinc;
        Y += Yinc;
        delay(100);
    }

    delay(10000000000);
    
}