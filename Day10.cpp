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

struct Node{
    int x,y;
    Node(int x,int y):x(x),y(y){}
};

void rec(int x,int y,vvi&arr,vvi&num_reach,int prev_value){
    if(x>=len(arr) || x<0 || y>=len(arr[0]) || y<0)return;
    if(arr[x][y]-prev_value!=-1)return;
    if(arr[x][y]==0){
        num_reach[x][y]=1;return;
    }
    range(i,0,4){
        rec(x+dx[i],y+dy[i],arr,num_reach,arr[x][y]);
    }
}

void solve1(){
    vvi arr;
    string line;
    while(getline(cin,line)){
        vi temp;
        for(auto&el:line){
            temp.pub(el-'0');
        }arr.pub(temp);
    }int n=len(arr),m=len(arr[0]);
    vector<Node> starts;
    range(i,0,n){
        range(j,0,m){
            if(arr[i][j]==9)starts.pub(Node(i,j));
        }
    }
    int ans=0;
    for(auto&el:starts){
        vvi num_reach(n,vi(m,0));
        rec(el.x,el.y,arr,num_reach,10);
        range(i,0,n){
            range(j,0,m){
                if(arr[i][j]==0)ans+=num_reach[i][j];
            }
        }
    }print(ans);
}

void rec2(int x,int y,vvi&arr,vvi&num_reach,int prev_value){
    if(x>=len(arr) || x<0 || y>=len(arr[0]) || y<0)return;
    if(arr[x][y]-prev_value!=-1)return;
    if(arr[x][y]==0){
        num_reach[x][y]+=1;return;
    }
    range(i,0,4){
        rec2(x+dx[i],y+dy[i],arr,num_reach,arr[x][y]);
    }
}

void solve2(){
    vvi arr;
    string line;
    while(getline(cin,line)){
        vi temp;
        for(auto&el:line){
            temp.pub(el-'0');
        }arr.pub(temp);
    }int n=len(arr),m=len(arr[0]);
    vector<Node> starts;
    range(i,0,n){
        range(j,0,m){
            if(arr[i][j]==9)starts.pub(Node(i,j));
        }
    }
    int ans=0;
    vvi num_reach(n,vi(m,0));
    for(auto&el:starts){
        rec2(el.x,el.y,arr,num_reach,10);
    }
    range(i,0,n){
        range(j,0,m){
            if(arr[i][j]==0)ans+=num_reach[i][j];
        }
    }
    print(ans);
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
