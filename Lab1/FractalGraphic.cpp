#include<stdio.h>
#include<graphics.h>
int main()
{
    int i,d,gd,gm,x,y;
    initgraph(&gd,&gm,NULL);
    delay(2000);
    x=150;
    y=150;
    for(i=0;i<1000;i++)
    {
        d=rand()%3;
        if(d==0)
        {
            x=(x+150)/2;
            y=y/2;
        }
        else if(d==1)
        {
            x=(x+300)/2;
            y=(y+150)/2;
        }
        else if(d==2)
        {
            x=x/2;
            y=(y+150)/2;
        }
        putpixel(x,y,WHITE);
    }
    delay(10000000000);
}