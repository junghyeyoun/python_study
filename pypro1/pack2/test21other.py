import pack2.test21singer

def process():
    jungkuk = pack2.test21singer.Singer()
    print('타이틀 송 : ',jungkuk.title_song)
    jungkuk.sing()
    jungkuk.title_song = '정국 찬양가'
    jungkuk.co = 'hive'
    print('소속사 가 '+jungkuk.co + '인 가수의 노래 '+jungkuk.title_song)

    print()
    iu = pack2.test21singer.Singer()   
    print('타이틀 송 : ',iu.title_song)
    iu.sing()
    # print('소속사 가 '+iu.co + '인 가수의 노래 '+iu.title_song) => err : iu는 co가 없기 때문에
    print(id(pack2.test21singer.Singer),id(iu)) # 2495509918336 2495508728144 다름
    
    print()
    bp = pack2.test21singer.Singer 
    print(id(pack2.test21singer.Singer),id(bp)) # 2307711105200 2307711105200 => 주소 같음
   # print(bp.sing()) # TypeError: Singer.sing() missing 1 required positional argument: 'self'
    
if __name__ == '__main__':
    process()
    
# 괄호가 있고 없고의 차이
# Singer()는 클래스를 인스턴스화하는 것이고, Singer는 클래스 자체를 가리키며 클래스의 정의를 나타냅니다. 
# 클래스를 인스턴스화하면 해당 클래스의 새로운 객체를 만들고, 클래스 자체를 사용하면 클래스를 변수에 할당하거나 다른 목적으로 사용할 수 있습니다.

# 괄호가 없는 경우, 즉 Singer는 클래스의 정의를 나타냅니다. 이것은 클래스를 변수에 할당하거나 클래스를 다른 변수에 할당하는 데 사용될 수 있습니다. 
# 예를 들면, bp = Singer와 같이 사용될 수 있습니다. 이 경우, bp는 Singer 클래스를 가리키는 변수가 됩니다. 
# 클래스 자체에는 인스턴스 속성 및 메서드에 직접 액세스할 수 없으므로 bp를 통해 인스턴스를 만들거나 사용해야 합니다.

# 괄호가 없는 경우, 즉 Singer()는 Singer 클래스를 인스턴스화하려는 것을 나타냅니다. 즉, 새로운 Singer 객체를 만들려는 것입니다. 
# 예를 들면, jungkuk = Singer()와 같이 사용될 수 있으며, jungkuk는 Singer 클래스의 새로운 인스턴스가 됩니다. 
# 이렇게 만들어진 인스턴스는 클래스의 속성과 메서드에 접근할 수 있습니다.