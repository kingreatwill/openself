package etcd
import (
	"context"
	"fmt"
	"go.etcd.io/etcd/clientv3"
	etcdnaming "go.etcd.io/etcd/clientv3/naming"
	"google.golang.org/grpc/balancer/roundrobin"

	"google.golang.org/grpc"
)
func xx(){
	conn, gerr := grpc.Dial(fmt.Sprintf("etcd:///%s", "my-service"), grpc.WithBlock(), grpc.WithDefaultServiceConfig(`{"loadBalancingPolicy":"round_robin"}`))

	/*
	客户端的重试机制和重试限流 (可以设置每个方法)都是通过 service config 来配置的，grpc.WithDefaultServiceConfig()
	https://github.com/grpc/grpc-go/tree/master/examples/features/retry

	https://github.com/grpc/grpc-go/tree/master/examples/features/load_balancing
	*/
}