class Singer():
    def __init__(self,sing_name,singer_name):
        self.sing_name = sing_name
        self.singer_name = singer_name
    def fans(self):
        print(f"{self.singer_name}歌手的{self.sing_name}歌曲持续打榜，粉丝为喜欢的歌手打call")

if __name__=="__main__":
    with open(r'data/singer.txt','r',encoding='utf-8') as f:
        singers = f.readlines()
        for singer in singers:
            s_n = singer.strip('\n').split(',')
            Singer(s_n[0],s_n[-1]).fans()
            # print(s_n)

# 沉默是金，张国荣歌手的沉默是金，张国荣歌曲持续打榜，粉丝为喜欢的歌手打call
# 少女的祈祷，杨千嬅歌手的少女的祈祷，杨千嬅歌曲持续打榜，粉丝为喜欢的歌手打call
# 暗里着迷，刘德华歌手的暗里着迷，刘德华歌曲持续打榜，粉丝为喜欢的歌手打call
# 难念的经，周华健歌手的难念的经，周华健歌曲持续打榜，粉丝为喜欢的歌手打call