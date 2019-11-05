#include <stdio.h>
#include <graphics.h>

int main()
{
	int gd = DETECT,gm,i;
	initgraph(&gd,&gm,NULL);
    //Cube
    line(100,200,200,200);
    line(100,200,100,300);
    line(200,200,200,300);
    line(100,300,200,300);

    line(100,200,150,150);
    line(200,200,250,150);
    line(150,150,250,150);
    line(250,250,200,300);

    line(250,150,250,250);

    //Shadow
    line(200,300,225,295);
    line(225,295,305,235);
    line(305,235,250,225);


	
     delay(10000000000);
}
