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

vi vi_input(){
    string line;
    vi arr;
    getline(cin, line);
    istringstream ss(line);
    int x;
    while(ss>>x)arr.pub(x);
    return arr;
}

vi get_input(char sep='|'){
    string line;
    getline(cin, line);
    if(len(line)==0){
        return {-1};
    }
    istringstream ss(line);
    string token;
    vi arr;
    while(getline(ss, token, sep)){
        arr.pub(stoi(token));
    }return arr;
}

void solve1(){
    umap<int,set<int>> constraints;
    while(1){
        vi cons=get_input();
        if(cons[0]==-1)break;
        constraints[cons[0]].insert(cons[1]);
    }
    vvi orders;
    while(1){
        vi order=get_input(',');
        if(order[0]==-1)break;
        orders.pub(order);
    }
    vi ans;
    for(auto&el: orders){
        bool flag=true;
        range(i,0,len(el)){
            range(j,i+1,len(el)){
                if(constraints[el[j]].count(el[i])){
                    flag=false;
                    break;
                }
            }
            if(!flag)break;
        }if(flag)ans.pub(el[len(el)/2]);
    }print(sum(ans));
}

void solve2(){
    umap<int,set<int>> constraints;
    while(1){
        vi cons=get_input();
        if(cons[0]==-1)break;
        constraints[cons[0]].insert(cons[1]);
    }
    vvi orders;
    while(1){
        vi order=get_input(',');
        if(order[0]==-1)break;
        orders.pub(order);
    }
    vi ans;
    for(auto&el: orders){
        bool flag=true;
        range(i,0,len(el)){
            range(j,i+1,len(el)){
                if(constraints[el[j]].count(el[i])){
                    flag=false;
                    break;
                }
            }
            if(!flag)break;
        }if(flag)continue;
        sort(all(el), [&](int a, int b){
            if(constraints[a].count(b))return true;
            return false;
        });ans.pub(el[len(el)/2]);
    }print(sum(ans));

}

 
int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    IO;
    int t=1;
    // cin>>t;
    range(_,0,t){
        solve2();
    }return 0;
}
