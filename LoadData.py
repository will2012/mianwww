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


def insetData():
    #array = loadData('c_contents.json')
    #array = loadData('linux_contents.json')
    #array = loadData('java_contents.json')
    #array = loadData('ios_contents.json')
    array = loadData('android_contents.json')

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
            #values.append((1, title, josn_rcms))
            #values.append((2, title, josn_rcms))
            #values.append((3, title, josn_rcms))
            #values.append((4, title, josn_rcms))
            values.append((5, title, josn_rcms))

        cur.executemany('insert into mian_post(category_id, post_title, post_content) values(%s, %s, %s)', values)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == "__main__":
    insetData()
