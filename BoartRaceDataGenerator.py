class BoartRaceDataGenerator:
    
    def __init__(self,target_file):
        #現在の走査行情報
        self.now_line = ""
        #現在の走査行番号
        self.now_line_num = 0
        #現在走査中のレースの基準行
        self.begin_line = ""
        #現在走査中のレースの基準行番号
        self.begin_line_num = 0
        
        
        self.tarminate_list = []
        
        #読み込み対象のCSVfile
        self.text_file = target_file
        
        #1レースの記述行数
        self.race_description_line = 21

    
    def _is_12race_start_tarminate_line(linestr):
        """ この行が12R情報の始行かどうかの判定するメソッド
        """
        if re.match(r'\d\dKBGN',linestr):
            return True
        else:
            return False
        
    def _is_12race_end_tarminate_line(linestr):
        """ この行が12R情報の終行かどうかの判定するメソッド
        """
        if re.match(r'\d\dKEND',linestr):
            return True
        else:
            return False
        
        
    def _set_tarminate_list(self):
        """ レース情報のtarminate情報を作成するメソッド
        """
        tarminate_num_list = []
        # 始行と終行の行番号を格納する
        with open(self.text_file, mode='rt', encoding='utf-8') as f:
            read_data = list(f)
            for line_num,line in enumerate(read_data):
                if _is_12race_start_tarminate_line(line) or _is_12race_end_tarminate_line(line)
                    tarminate_list.append(line_num)
        
        # 取得した行番号をグルーピングする
        start_num = 0
        end_num = 0
        result = []
        for tarminate_num in tarminate_num_list:
            if start_num == 0 and end_num == 0
                start_num = tarminate_num
            elif start_num != 0 and end_num == 0
                end_num = tarminate_num
            else start_num != 0 and end_num != 0:
                result.append([start_num, end_num])
                start_num = 0
                end_num = 0
                
        self.tarminate_list = result
        
        
        
        
        
    # 基準行のlineで開催場所のコードを取得
    def _get_place_num(self):
        return int(self.base_line[0:2])

    # 基準行をベースにタイトル行か判定
    def _is_title_line(self):
        if (self.now_line_num == self.begin_line_num + 5
            or self.now_line_num == self.begin_line_num + 5 + self.race_description_line
            or self.now_line_num == self.begin_line_num + 5 + self.race_description_line * 2
            or self.now_line_num == self.begin_line_num + 5 + self.race_description_line * 3
            or self.now_line_num == self.begin_line_num + 5 + self.race_description_line * 4
            or self.now_line_num == self.begin_line_num + 5 + self.race_description_line * 5):
            return True
        else:
            return False

    # タイトル行からタイトルを取得
    def _get_title(self):
        return self.strip_blank(self.now_line)

    # 基準行をベースにレース開催日記載行か判定
    def _is_race_day_line(self):
        if self.now_line_num == self.begin_line_num + 7:
            return True
        else:
            return False
    # レースの開催n日目の情報かを取得
    def _get_race_day_line(self):
        return int(self.delete_blank(self.now_line[(self.now_line.find("第"))+1:(self.now_line.find("日"))]))
    
    # 基準行をベースにタイトル行か判定
    def _is_race_about_info(self):
        if self.now_line_num == self.begin_line_num + 27:
            return True
        else:
            return False
        
        
    # racer
    def _is_race_result(self):
        if self.now_line_num >= self.begin_line_num + 30 and self.now_line_num <= self.begin_line_num + 35:
            return True
        else:
            return False
    
    
    
    
    
    def delete_blank(self, string):
        return string.replace(" ","").replace("　","")
    
    def test_run(self):
        
        with open(self.text_file, mode='rt', encoding='utf-8') as f:

            # [**KBGN]を処理始まり行(0行目)とする
            # **は会場番号

            ## 5行目 タイトル
            ## ７行目 何日目か　開催日　場所名
            ## 12行〜23行目　払戻金情報

            ### 27行目 天候　風方角　風力　波
            ### 30~３５　1Rレース結果
            ### 37~45 配当と人気


            read_data = list(f)

            for line_num,line in enumerate(read_data):
                self.now_line_num = line_num
                self.now_line = line

                print(line)

                if self._is_race_start_line():
                    print("基準行だよ")
                    self.begin_line_num = line_num
                if self._is_title_line():
                    print("タイトル行だよ")
                if self._is_race_day_line():
                    print("レース何日目の行だよ")
                    print(self._get_race_day_line())
                if self._is_race_about_info():
                    print(self.now_line.split())
                    print("about行だよ")
                if self._is_race_result():
                    
                    print("着艇:" + self.now_line[2:4])
                    print("登板:" + self.now_line[6:7])
                    print("選手ID:" + self.now_line[8:12])
                    print("選手名:" + self.delete_blank(self.now_line[13:20]))
                    #名前移行はsplitで取得可能
                    print("モータ:" + self.now_line[21:].split()[0])
                    print("ボート:" + self.now_line[21:].split()[1])
                    print("展示:" + self.now_line[21:].split()[2])
                    print("進入:" + self.now_line[21:].split()[3])
                    print("スタートタイミング:" + self.now_line[21:].split()[4])
                    print("レースタイム:" + self.now_line[21:].split()[5])
                    
                    print("選手の結果行")
                if line_num>100:
                    break