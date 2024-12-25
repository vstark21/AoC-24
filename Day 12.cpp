#include <iostream>
#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
using namespace std;
 
namespace custom{
    typedef long long ll;
    typedef long double ld;
    typedef pair<int,int> pii;
    typedef pair<ll,ll> pll;
    typedef pair<ld,ld> pld;
    typedef vector<int> vi;
    typedef vector<vi> vvi;
    typedef vector<ll> vll;
    typedef vector<vll> vvll;
    typedef vector<pii>vpii;
    typedef vector<pll> vpll;
    
    #define pub push_back
    #define puf push_front
    #define pob pop_back
    #define fi first 
    #define se second
    #define precision(a) fixed<<setprecision(a)
    #define init(var,val) memset(var,val,sizeof(var))
    #define range(i, init, n) for(int i=init;i<n;i+=1)
    #define all(arr) arr.begin(),arr.end()
    #define INF INT_MAX
    #define LINF LONG_LONG_MAX
    #define IO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
    #define MOD 1000000007
    const int dx[4]={-1,0,1,0};
    const int dy[4]={0,1,0,-1};
 
    template<class T>
    istream& operator>>(istream& in, vector<T>& v){
        for(auto&el:v)in>>el;
        return in;
    }
    template<class T>
        void print(T a,string end="\n"){cout<<a<<end;}
    template<class T1, class T2> 
        void print(pair<T1,T2>& a,string end="\n"){
            cout<<"{"<<a.fi<<","<<a.se<<"}"<<end;
        }
    template<class T> 
        void parr(T& arr, string end="\n"){
            int i=0;
            for(auto&el:arr){
                print(el," ");}
            print("",end);
        }
    template<class T> 
        void print(vector<T>& a,string end="\n"){parr(a,end);}
    template<class T> 
        void print(set<T>& a,string end="\n"){parr(a,end);}
    template<class T> 
        void print(deque<T>& a,string end="\n"){parr(a,end);}
    template<class T1, class T2> 
        void print(map<T1,T2>& a,string end="\n"){
            int i=0;
            for(auto&el:a){
                print(el.fi," : ");print(el.se);
            }print("",end);
        }
    template<class T>
        void _print(T f,string end){
            print(f,end);
        }
    template<class arg1, class... args> 
        void print(arg1 f, args... n){
            _print(f," ");print(n...);}
    template<class T> 
        void print(vector<vector<T>>& a){
            for(auto&el:a)print(el,"\n");
        }
    template<class T> int len(T& a){return a.size();}
    template<class T>
        ll sum(T& a){
            ll s=0;for(auto&el:a)s+=el;
            return s;
        }
    template<class T1,class T2> T1 min(T1 a,T2 b){
        return (a<b)?a:(T1)b;
    }template<class T1,class T2> T1 max(T1 a,T2 b){
        return (a>b)?a:(T1)b;
    }template<class T> T max(vector<T>a){
        T m=a[0];for(auto&el:a)m=max(m,el);
        return m;
    }template<class T> T min(vector<T>a){
        T m=a[0];for(auto&el:a)m=min(m,el);
        return m;
    }
    template<class T1, class... T2>
        T1 min(T1 a, T2... b){
            return min(a, (T1)min(b...));
        }
    template<class T1, class... T2>
        T1 max(T1 a, T2... b){
            return max(a, (T1)max(b...));
        }
    // template<class T>
    // using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
    // template<class T>
    // using multiordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, tree_order_statistics_node_update>;
    // order_of_key,find_by_order
}using namespace custom;
#define umap unordered_map
#define graph vector<vector<char>>

int check_perimeter(int x,int y,graph& arr){
    int cnt=0;
    range(i,0,4){
        int nx=x+dx[i],ny=y+dy[i];
        if(nx<0||ny<0||nx>=len(arr)||ny>=len(arr[0])||arr[nx][ny]!=arr[x][y])cnt+=1;
    }return cnt;
}

void rec(int x,int y,graph& arr,vvi& vis,ll& area,ll& per,char&prev){
    if(x<0||y<0||x>=len(arr)||y>=len(arr[0]))return;
    if(arr[x][y]!=prev)return;
    if(vis[x][y])return;
    vis[x][y]=1;
    area+=1;
    per+=check_perimeter(x,y,arr);
    range(i,0,4)rec(x+dx[i],y+dy[i],arr,vis,area,per,prev);    
}

void solve1(){
    graph arr;
    string line;
    while(getline(cin,line)){
        arr.pub(vector<char>(all(line)));
    }int n=len(arr),m=len(arr[0]);
    vvi vis(n,vi(m,0));
    ll ans=0;
    range(i,0,n){
        range(j,0,m){
            if(vis[i][j])continue;
            ll area=0,per=0;
            rec(i,j,arr,vis,area,per,arr[i][j]);
            ans+=(area*per);
        }
    }print(ans);
}

struct Node{
    int x,y;
    Node(int x,int y):x(x),y(y){}
};

void check_per(int x,int y,graph& arr,vector<Node>&left,vector<Node>&right,vector<Node>&top,vector<Node>&bot){
    range(i,0,4){
        int nx=x+dx[i],ny=y+dy[i];
       if(nx<0||ny<0||nx>=len(arr)||ny>=len(arr[0])||arr[nx][ny]!=arr[x][y]){
            if(i==0)top.pub(Node(nx,ny));
            if(i==1)right.pub(Node(nx,ny));
            if(i==2)bot.pub(Node(nx,ny));
            if(i==3)left.pub(Node(nx,ny));
       }
    }
}

void rec2(int x,int y,graph& arr,vvi& vis,ll& area,char&prev,vector<Node>&left,vector<Node>&right,vector<Node>&top,vector<Node>&bot){
    if(x<0||y<0||x>=len(arr)||y>=len(arr[0]))return;
    if(arr[x][y]!=prev)return;
    if(vis[x][y])return;
    vis[x][y]=1;
    area+=1;
    check_per(x,y,arr,left,right,top,bot);
    range(i,0,4)rec2(x+dx[i],y+dy[i],arr,vis,area,prev,left,right,top,bot);    
}

void update_left_right(vector<Node>& some,ll& per){
    sort(all(some),[](Node& a,Node& b){
        if(a.y==b.y)return a.x<b.x;
        return a.y<b.y;
    });
    per+=(some.size()>0);
    range(i,1,len(some)){
        if(some[i].y!=some[i-1].y)per+=1;
        else{
            if(some[i].x-some[i-1].x>1)per+=1;
        }
    }
}

void update_top_bot(vector<Node>& some,ll& per){
    sort(all(some),[](Node& a,Node& b){
        if(a.x==b.x)return a.y<b.y;
        return a.x<b.x;
    });
    per+=(some.size()>0);
    range(i,1,len(some)){
        if(some[i].x!=some[i-1].x)per+=1;
        else{
            if(some[i].y-some[i-1].y>1)per+=1;
        }
    }
}

void solve2(){
    graph arr;
    string line;
    while(getline(cin,line)){
        arr.pub(vector<char>(all(line)));
    }int n=len(arr),m=len(arr[0]);
    vvi vis(n,vi(m,0));
    ll ans=0;
    range(i,0,n){
        range(j,0,m){
            if(vis[i][j])continue;
            ll area=0,per=0;
            vector<Node> left,right,top,bot;
            rec2(i,j,arr,vis,area,arr[i][j],left,right,top,bot);
            update_left_right(left,per);update_left_right(right,per);update_top_bot(top,per);update_top_bot(bot,per);
            ans+=(area*per);
        }
    }print(ans);
}

int main(){
    auto start=chrono::high_resolution_clock::now();

    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    IO;
    int t=1;
    // cin>>t;
    range(_,0,t){
        solve2();
    }
    auto stop=chrono::high_resolution_clock::now();
    auto duration=chrono::duration_cast<chrono::microseconds>(stop-start);
    print("Time Taken: ",(double)duration.count()/1e6," seconds");

    return 0;
}
