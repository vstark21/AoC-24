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

void update_ans(int& cur_id,int& spos,int le,ll& ans){
    ll cur_ans=spos*le+(le*(le-1))/2;
    cur_ans*=cur_id;
    ans+=cur_ans;
}

int ctoi(char& c){
    return c-'0';
}

void solve1(){
    string s;cin>>s;
    umap<int,int> cid_mp,space_mp;
    int cur_id=0;
    int f=0,n=len(s);
    while(f<n){
        cid_mp[cur_id]=ctoi(s[f]);
        f+=2;cur_id+=1;
    }int lcur_id=cur_id-1;
    f=1;
    while(f<n){
        space_mp[f]=ctoi(s[f]);f+=2;
    }f=1;int scur_id=0,spos=0;
    ll ans=0;
    while(scur_id<lcur_id){
        update_ans(scur_id,spos,cid_mp[scur_id],ans);spos+=cid_mp[scur_id];
        cid_mp[scur_id]=0;
        scur_id+=1;
        while(1){
            int le=min(space_mp[f],cid_mp[lcur_id]);
            update_ans(lcur_id,spos,le,ans);
            spos+=le;
            space_mp[f]-=le;
            cid_mp[lcur_id]-=le;
            if(cid_mp[lcur_id]==0)lcur_id-=1;
            if(space_mp[f]==0){
                f+=2;break;
            }
        }
    }update_ans(scur_id,spos,cid_mp[scur_id],ans);
    print(ans);
}

void solve2(){
    string s;cin>>s;
    umap<int,int> cid_mp;
    int cur_id=0;
    int f=0,n=len(s);
    while(f<n){
        cid_mp[cur_id]=ctoi(s[f]);
        f+=2;cur_id+=1;
    }f=0;cur_id=0;int spos=0;ll ans=0;
    while(f<n){
        update_ans(cur_id,spos,cid_mp[cur_id],ans);
        spos+=ctoi(s[f]);cid_mp[cur_id]=0;cur_id+=1;
        f+=1;int space=ctoi(s[f]);
        int lcur_id=len(cid_mp)-1;
        while(lcur_id>=cur_id && space>0){
            if(space>=cid_mp[lcur_id]){
                update_ans(lcur_id,spos,cid_mp[lcur_id],ans);
                spos+=cid_mp[lcur_id];space-=cid_mp[lcur_id];
                cid_mp[lcur_id]=0;
            }lcur_id-=1;
        }f+=1;spos+=space;
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
