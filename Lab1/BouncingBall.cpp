#include<stdio.h>
#include<graphics.h>
#include<math.h>
int main()
{
    int gd=DETECT,gm,r=10;
    initgraph(&gd,&gm,NULL);
    

    float x=300,y,b=1,count=0.1,i;
    setcolor(WHITE);
    for(int n=0;n<7;n++){
        for(i=0;i<180;i+=10){
            y=sin(i*3.14/180)/b;
            y=-y;
            circle(x,y*100+300,r);
            r+=2;
            delay(50);
            cleardevice();
        }
        b*=0.7;
    }
    delay(1000000000000000);
    closegraph();
}