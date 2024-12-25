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

pair<ll,ll> split(ll a){
    string b=to_string(a);
    int n=len(b);
    ll a1=0,a2=0;int i=0;while(i<n/2)a1=a1*10+b[i++]-'0';
    while(i<n)a2=a2*10+b[i++]-'0';
    return {a1,a2};
}

bool is_len_even(ll& a){
    int l=log10(a)+1;
    return l%2==0;
}

void solve1(){
    string line;
    getline(cin,line);
    vll arr;ll x;
    stringstream ss(line);while(ss>>x)arr.pub(x);
    int n_steps=25;
    range(_,0,n_steps){
        vll new_arr;
        for(auto&el:arr){
            if(el==0)new_arr.pub(1);
            else if(is_len_even(el)){
                auto [c,d]=split(el);
                new_arr.pub(c);new_arr.pub(d);
            }else{
                new_arr.pub(el*2024);
            }
        }arr=new_arr;
    }print(len(arr));
}

ll rec(ll a, vector<umap<ll,ll>>& num_stones,int num_step){
    if(num_step==0)return 1;
    else if(num_stones[num_step].count(a))return num_stones[num_step][a];
    else if(a==0)return num_stones[num_step][a]=rec(1,num_stones,num_step-1);
    else if(is_len_even(a)){
        auto [c,d]=split(a);
        num_stones[num_step][a]=rec(c,num_stones,num_step-1)+rec(d,num_stones,num_step-1);
    }else{
        num_stones[num_step][a]=rec(a*2024,num_stones,num_step-1);
    }return num_stones[num_step][a];
}

void solve2(){
    string line;
    getline(cin,line);
    vll arr;ll x;
    stringstream ss(line);while(ss>>x)arr.pub(x);
    int total_steps=75;
    ll ans=0;
    vector<umap<ll,ll>> num_stones(total_steps+1);
    range(n_steps,1,total_steps+1){
        for(auto&el: arr){
            rec(el,num_stones,n_steps);
        }
    }for(auto&el:arr)ans+=num_stones[total_steps][el];
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
