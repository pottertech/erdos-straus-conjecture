#include <bits/stdc++.h>
using namespace std; using U=uint64_t; using W=__uint128_t;
vector<uint16_t> sp;
vector<pair<int,int>> fac(int x){vector<pair<int,int>> f; while(x>1){int q=x%2==0?2:(sp[x/2]?sp[x/2]:x),e=0; do{x/=q;e++;}while(x%q==0); f.push_back({q,e});}return f;}
int first(int p){for(int u=3;u<=251;u+=4){int x=(p+u)/4; U M=(U)p*x; if(gcd(M,(U)u)!=1)continue; W d[252]={}, n[252]={}; d[1]=1; auto f=fac(x);f.push_back({p,1}); for(auto [q,e]:f){fill(n,n+u,0);W power=1; int qr=1; for(int j=0;j<=2*e;j++){for(int r=0;r<u;r++)if(d[r])n[(r*qr)%u]=d[r]*power; if(j<2*e)power*=q;qr=(U)qr*q%u;}copy(n,n+u,d);} W P=d[(u-M%u)%u];if(!P)continue; W S=(W)M*M,Q=S/P; assert(P*Q==S && (P+M)%u==0 && (Q+M)%u==0); W y=(P+M)/u,z=(Q+M)/u; assert(y>0&&z>0);return u;}return 0;}
struct Class { bool par=false,non=false,firstpar=false; };
Class classify(int p,int u) {
 int x=(p+u)/4; U M=(U)p*x; int target=(u-M%u)%u; Class c;
 vector<U> ds{1}; for(auto [q,e]:fac(x)){size_t old=ds.size(); U pow=1; for(int j=1;j<=2*e;j++){pow*=q; for(size_t k=0;k<old;k++)ds.push_back(ds[k]*pow);}}
 sort(ds.begin(),ds.end()); bool got=false;
 auto check=[&](W d){if(d>M||d%u!=target)return; U D=(U)d; bool par=M%D==0; if(!got){c.firstpar=par;got=true;} if(par)c.par=true; else c.non=true;};
 for(U a: {U(1),U(p),U(p)*p})for(U b:{U(1),U(x),U(x)*x})check(W(a)*b);
 for(U a: {U(1),U(p),U(p)*p})for(U b:ds){W d=W(a)*b;if(d>M)break;check(d);}
 assert(got);return c;
}
int main(int argc,char**argv){int hi=argc>1?atoi(argv[1]):999999999;int X=(hi+251)/4;sp.resize(X/2+1); for(int q=3;(U)q*q<=X;q+=2)if(!sp[q/2])for(U j=(U)q*q;j<=X;j+=2*q)if(!sp[j/2])sp[j/2]=q; cerr<<"factor sieve ready\n"; vector<bool> comp(hi/12+1);for(int q=5;(U)q*q<=hi;q+=2)if(!sp[q/2]){int r=0;while((12*r+1)%q)r++; U k=r; if(12*k+1==q)k+=q;for(;k<comp.size();k+=q)comp[k]=true;}
 cerr<<"prime sieve ready\n"; U cnt[2][252]={}, full[252]={};int maxu[2]={},maxp[2]={},maxfull=0,maxfullp=0;U mod840[3]={},h24classes[3]={},res[840]={},resnop[840]={}; U classes[2][4]={}; U intrinsic[2][3]={}; U pop[2]={},h24[2]={},fullpop=0,fullh24=0; for(int k=1;k<(int)comp.size();k++){if(comp[k])continue;int p=12*k+1;if(p>hi)break;if(p<=10000000){int u=first(p);full[u]++;fullpop++;fullh24+=p%24==1;if(u>maxfull){maxfull=u;maxfullp=p;}continue;}auto f=fac((p+3)/4);bool ok=true;for(auto [q,e]:f)if(q!=2&&q%3!=1){ok=false;break;}if(!ok)continue;int u=first(p);assert(u); auto c=classify(p,u); int cls=c.par?(c.non?1:0):2; if(p%24==1)h24classes[cls]++; int r=p%840; if(r==1||r==121||r==169||r==289||r==361||r==529){mod840[cls]++;res[r]++;if(cls==2)resnop[r]++;} if(u==83)cerr<<"MAX83 "<<p<<"\n";for(int i=0;i<2;i++){if(i==1&&p<100000000)continue;classes[i][c.firstpar?0:c.par?1:2]++;intrinsic[i][c.par?(c.non?1:0):2]++;pop[i]++;h24[i]+=p%24==1;cnt[i][u]++;if(u>maxu[i]){maxu[i]=u;maxp[i]=p;}}}
 cout<<"H24 "<<h24classes[0]<<" "<<h24classes[1]<<" "<<h24classes[2]<<"\n"; cout<<"MOD840 "<<mod840[0]<<" "<<mod840[1]<<" "<<mod840[2]<<"\n"; for(int r=0;r<840;r++)if(res[r])cout<<"RES "<<r<<" "<<res[r]<<" "<<resnop[r]<<"\n"; for(int i=0;i<2;i++){cout<<"CLASS "<<i<<" "<<classes[i][0]<<" "<<classes[i][1]<<" "<<classes[i][2]<<" INTRINSIC "<<intrinsic[i][0]<<" "<<intrinsic[i][1]<<" "<<intrinsic[i][2]<<"\n";} cout<<"FULL "<<fullpop<<" H24 "<<fullh24<<" MAX "<<maxfull<<" AT "<<maxfullp<<"\n";for(int u=0;u<=251;u++)if(full[u])cout<<u<<":"<<full[u]<<" ";cout<<"\n"; for(int i=0;i<2;i++){cout<<"SWEEP "<<i<<" POP "<<pop[i]<<" H24 "<<h24[i]<<" MAX "<<maxu[i]<<" AT "<<maxp[i]<<"\n";for(int u=0;u<=251;u++)if(cnt[i][u])cout<<u<<":"<<cnt[i][u]<<" ";cout<<"\n";}}
