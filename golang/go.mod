module github.com/openjw/openself/golang

go 1.15

replace (
    google.golang.org/grpc => github.com/grpc/grpc-go v1.31.0

)

require google.golang.org/grpc v1.31.0 // indirect
