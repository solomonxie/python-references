# brew install rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management

# user:password -> "guest":"guest"
open http://localhost:15672
