#include <stdio.h>
#include <graphics.h>

int main()
{
	int gd = DETECT,gm,i;
	initgraph(&gd,&gm,NULL);

	for(i=0;i<4;i++){
		
		//standing position
		setcolor(WHITE);
		line(200,300,200,150); //body
		circle(200,100,50); //head
		line(150,400,200,300); //left leg
		line(250,400,200,300); //right leg
		line(200,200,150,200); //left arm
		line(200,200,250,200); //right arm
		setcolor(BLACK);
		line(100,150,150,200); //left forearm
		line(300,250,250,200); //right forearm
		line(125,400,150,400); //left foot
		line(225,400,250,400); //right foot
		setcolor(WHITE);
		line(100,150,150,200); //left forearm
		line(300,150,250,200); //right forearm
		line(125,400,150,400); //left foot
		line(275,400,250,400); //right foot
		delay(500);
		cleardevice();
		
		//Position1
		setcolor(WHITE);
		line(200,300,200,150); //body
		circle(200,100,50); //head
		line(150,400,200,300); //left leg
		line(250,400,200,300); //right leg
		line(200,200,150,200); //left arm
		line(200,200,250,200); //right arm
		setcolor(BLACK);
		line(100,150,150,200); //left forearm
		line(300,150,250,200); //right forearm
		line(125,400,150,400); //left foot
		line(275,400,250,400); //right foot
		setcolor(WHITE);
		line(100,250,150,200); //left forearm
		line(300,150,250,200); //right forearm
		line(125,400,150,400); //left foot
		line(275,400,250,400); //right foot
		delay(500);
		
		//Position2
		setcolor(WHITE);
		line(200,300,200,150); //body
		circle(200,100,50); //head
		line(150,400,200,300); //left leg
		line(250,400,200,300); //right leg
		line(200,200,150,200); //left arm
		line(200,200,250,200); //right arm
		setcolor(BLACK);
		line(100,250,150,200); //left forearm
		line(300,150,250,200); //right forearm
		line(175,400,150,400); //left foot
		line(275,400,250,400); //right foot
		setcolor(WHITE);
		line(100,250,150,200); //left forearm
		line(300,250,250,200); //right forearm
		line(125,400,150,400); //left foot
		line(275,400,250,400); //right foot
		delay(500);
		cleardevice();

		//squat position
		setcolor(BLACK);
		line(200,300,200,150); //body
		circle(200,100,50); //head
		line(150,400,200,300); //left leg
		line(250,400,200,300); //right leg
		line(200,200,150,200); //left arm
		line(200,200,250,200); //right arm
		setcolor(WHITE);
		line(200,350,200,200); //body
		circle(200,150,50); //head
		line(125,400,200,350); //left leg
		line(275,400,200,350); //right leg
		line(200,250,150,250); //left arm
		line(200,250,250,250); //right arm
		setcolor(BLACK);
		line(100,150,150,200); //left forearm
		line(300,150,250,200); //right forearm
		line(125,400,150,400); //left foot
		line(275,400,250,400); //right foot
		setcolor(WHITE);
		line(100,200,150,250); //left forearm
		line(300,200,250,250); //right forearm
		line(125,400,100,400); //left foot
		line(275,400,300,400); //right foot
		delay(500);
		cleardevice();
		
		//Position3
		setcolor(WHITE);
		line(200,350,200,200); //body
		circle(200,150,50); //head
		line(125,400,200,350); //left leg
		line(275,400,200,350); //right leg
		line(200,250,150,250); //left arm
		line(200,250,250,250); //right arm
		setcolor(BLACK);
		line(100,300,150,250); //left forearm
		line(300,200,250,250); //right forearm line(300,150,250,200);
  		line(125,400,150,400); //left foot
		line(275,400,250,400); //right foot
		setcolor(WHITE);
		line(100,200,150,250); //left forearm
		line(300,300,250,250); //right forearm line(300,200,250,250);
		line(125,400,100,400); //left foot
		line(275,400,300,400); //right foot
		delay(500);
		cleardevice();
		
		//Position4
		setcolor(WHITE);
		line(200,350,200,200); //body
		circle(200,150,50); //head
		line(125,400,200,350); //left leg
		line(275,400,200,350); //right leg
		line(200,250,150,250); //left arm
		line(200,250,250,250); //right arm
		setcolor(BLACK);
		line(100,200,150,250); //left forearm line(100,150,150,200); //left forearm
		line(300,300,250,250); //right forearm
		line(125,400,150,400); //left foot
		line(275,400,250,400); //right foot
		setcolor(WHITE);
		line(100,300,150,250); //left forearm line(100,250,150,200); //left forearm
 		line(300,300,250,250); //right forearm
		line(125,400,100,400); //left foot
		line(275,400,300,400); //right foot
		delay(500);
		cleardevice();
		
	}
	delay(1000000000000);
	closegraph();
}