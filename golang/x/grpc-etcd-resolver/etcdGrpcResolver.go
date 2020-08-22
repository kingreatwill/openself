package grpc_etcd_resolver

import "google.golang.org/grpc/resolver"

const (
	scheme      = "etcd"
	serviceName = "lb.example.grpc.io"
)

var addrs = []string{"localhost:50051", "localhost:50052"}

type etcdGrpcResolverBuilder struct{}

func (*etcdGrpcResolverBuilder) Build(target resolver.Target, cc resolver.ClientConn, opts resolver.BuildOptions) (resolver.Resolver, error) {
	r := &etcdGrpcResolver{
		target: target,
		cc:     cc,
		addrsStore: map[string][]string{
			serviceName: addrs,
		},
	}
	r.start()
	return r, nil
}
func (*etcdGrpcResolverBuilder) Scheme() string { return scheme }

type etcdGrpcResolver struct {
	target     resolver.Target
	cc         resolver.ClientConn
	addrsStore map[string][]string
}

func (r *etcdGrpcResolver) start() {
	addrStrs := r.addrsStore[r.target.Endpoint]
	addrs := make([]resolver.Address, len(addrStrs))
	for i, s := range addrStrs {
		addrs[i] = resolver.Address{Addr: s}
	}
	// 监听etcd
	r.cc.UpdateState(resolver.State{Addresses: addrs})
}
func (*etcdGrpcResolver) ResolveNow(o resolver.ResolveNowOptions) {}
func (*etcdGrpcResolver) Close()                                  {}

func init() {
	resolver.Register(&etcdGrpcResolverBuilder{})
}
