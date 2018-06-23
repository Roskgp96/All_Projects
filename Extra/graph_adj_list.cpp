#include<stdio.h>
#include<iostream>
using namespace std;
struct node{
int data;
struct node* next;
};
struct listi{
struct node* head;
};
struct graphi{
int V;
struct listi* array;
};
struct node* createnode(int dat)
{
node* newnode=new node;
newnode->data=dat;
newnode->next=NULL;
return newnode;
}
struct graphi* creategraph(int V)
{
graphi* newgraph=new graphi;
newgraph->array=new listi[V];
newgraph->V=V;
for (int i=0;i<V;++i)
newgraph->array[i].head=NULL;

return newgraph;
}

void addEdge(struct graphi* Graph,int src,int dest)
{
struct node* nodei=createnode(dest);
struct node* nodej=createnode(src);
if (Graph->array[src].head!=NULL)
{
nodei->next=Graph->array[src].head;
Graph->array[src].head=nodei;
}
else
{
Graph->array[src].head=nodei;
}
if (Graph->array[dest].head!=NULL)
{
nodej->next=Graph->array[dest].head;
Graph->array[dest].head=nodej;
}
else
{
Graph->array[dest].head=nodej;
}
}

void printgraph(struct graphi* Graph)
{
int V=Graph->V;
for (int i=0;i<V;++i)
{
struct node* p=Graph->array[i].head;
while(p)
{
cout<<p->data;
p=p->next;
}
cout<<endl;
}
cout<<'L'<<endl;
}
void bfsprint(struct node* temp,int V,bool* visited)
{
int i=0;
int flag=0;
struct node** temp2=new node*[V];
while(temp)
{
temp2[i]=temp;
temp=temp->next;
i=i+1;

}
for(int j=0;j<i;j++)
{
if (!visited[temp2[j]->data])
{
cout<<temp2[j]->data<<endl;
visited[temp2[j]->data]=1;
flag=1;
}
}
if (flag==1)
{
for(int k=0;k<i;k++)
bfsprint(temp2[k],V,visited);
}
}
void BFS(struct graphi* Graph,int x)
{
int V=Graph->V;
bool *visited=new bool[V];
for(int i=0;i<V;i++)
visited[i]=0;
node* temp=new node;
temp=Graph->array[x].head;

int i=0;
bfsprint(temp,V,visited);


}


int main()
{
int V=5;
struct graphi* Graph=creategraph(V);
addEdge(Graph, 0, 1);
addEdge(Graph, 0, 4);
addEdge(Graph, 1, 2);
addEdge(Graph, 1, 3);
addEdge(Graph, 1, 4);
addEdge(Graph, 2, 3);
addEdge(Graph, 3, 4);
printgraph(Graph);
BFS(Graph,1);
}


