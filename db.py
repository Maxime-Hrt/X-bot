import sqlite3


class DB:
    def __init__(self):
        self.con = None
        self.cur = None
        try:
            self.con = sqlite3.connect("Reco-Travel-Bot")
            self.cur = self.con.cursor()
        except Exception as e:
            print(f'Connection failed: {e}')

    def add_tweet(self, tweet_task):
        sql = """ 
            INSERT INTO tweets
            (tweet_id, location_name, country, posting_date) VALUES(?, ?, ?, ?)
            """
        self.cur.execute(sql, tweet_task)
        self.con.commit()

        return self.cur.lastrowid

    def delete_tweet_by_location(self, location):
        sql = """
            DELETE FROM tweets WHERE location_name=?
            """
        self.cur.execute(sql, (location,))
        self.con.commit()

# cur.execute("CREATE TABLE tweets(tweet_id, location_name, country, posting_date);")
