## go mod
go.etcd.io/etcd => github.com/etcd-io/etcd
golang.org/x/net => github.com/golang/net

## etcd
等3.5做（规范问题以及不支持grpc v1.30.0）
> https://github.com/etcd-io/etcd/issues/11154#issuecomment-620886957

https://github.com/mbobakov/grpc-consul-resolver
```
package etcd
import (
	"context"
	"go.etcd.io/etcd/clientv3"
	etcdnaming "go.etcd.io/etcd/clientv3/naming"
	"google.golang.org/grpc/balancer/roundrobin"

	"google.golang.org/grpc"
)
func xx(){
	// grpc 服务注册与发现 https://etcd.io/docs/v3.4.0/dev-guide/grpc_naming/
	cli, cerr := clientv3.NewFromURL("http://localhost:2379")
	r := &etcdnaming.GRPCResolver{Client: cli}
	b := grpc.RoundRobin(r)
	conn, gerr := grpc.Dial("my-service", grpc.WithBalancer(b), grpc.WithBlock(), )

	/*
	客户端的重试机制和重试限流 (可以设置每个方法)都是通过 service config 来配置的，grpc.WithDefaultServiceConfig()
	https://github.com/grpc/grpc-go/tree/master/examples/features/retry

	https://github.com/grpc/grpc-go/tree/master/examples/features/load_balancing
	*/
	// RoundRobin WithBalancer 在新版本已经删除了 https://github.com/googleapis/google-api-go-client/issues/441
	r.Update(context.TODO(), "my-service", naming.Update{Op: naming.Add, Addr: "1.2.3.4", Metadata: "..."})

	r.Update(context.TODO(), "my-service", naming.Update{Op: naming.Delete, Addr: "1.2.3.4"})

	// 带租约
}
```