//C program to implement Bresenham straight line drawing algorithm
#include<stdio.h>
#include<graphics.h>
int main()
{
    int gd = DETECT, gm;
    int x1, y1, x2, y2, dx, dy, p;
    float m, Xinc, Yinc, X, Y;

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
    m = (float)dy / (float)dx;

    X = x1;
    Y = y1;
    initgraph(&gd,&gm,NULL);
    
    //Positive slope
    if(m > 0)
    {
        p = 2*dy - dx;
        while(X < x2)
        {
            if(p >= 0)
            {
                putpixel(X,Y,WHITE);
                Y = Y + 1;
                p = p + 2*dy - 2*dx;
                delay(100);
            }
            else
            {
                putpixel(X,Y,WHITE);
                p = p + 2*dy;
                delay(100);
            }
            X = X + 1;
        }
    }
    
    //Negative slope
    else if(m < 0)
    {
        p = 2*dy - dx;
        while(X < x2)
        {
            if(p < 0)
            {
                putpixel(X,Y,GREEN);
                Y = Y - 1;
                p = p + 2*dy - 2*dx;
                delay(100);
            }
            else
            {
                putpixel(X,Y,GREEN);
                p = p + 2*dy;
                delay(100);
            }
            X = X + 1;
        }
    }
    delay(10000000000);    
}