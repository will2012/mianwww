import MySQLdb
import json
def loadData(filepath):
    file_object = open(filepath)
    try:
        jsonstr = file_object.read()
        array = json.loads(jsonstr)
        return array
        for item in array:
            pass
    finally:
        file_object.close()


def insetData(filepath, ctype):
    array = loadData(filepath)

    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='AAAaaa111',db='mian',port=3306,charset='utf8')
        cur=conn.cursor()
        values=[]
        for item in array:
            title = item['title'].encode('utf-8')
            contents = item['contents']
            #for content in contents:
            #    print content.encode('utf-8')
            #contents = '';#json.dumps(item['contents']).encode('utf-8')
            josn_rcms = json.dumps(contents,ensure_ascii=False)
            #print title, josn_rcms
            values.append((ctype, title, josn_rcms))

        cur.executemany('insert into mian_post(category_id, post_title, post_content) values(%s, %s, %s)', values)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == "__main__":
     #insetData('c_contents.json', 1);
     #insetData('linux_contents.json', 2);
     #insetData('ios_contents.json', 4);
     #insetData('android_contents.json', 5);
     insetData('cpp_contents.json', 6);
     insetData('softtest_contents.json', 7);
