from database.DB_connect import DBConnect
from model.team import Team

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():

        conn=DBConnect.get_connection()
        cursor=conn.cursor(dictionary=True)

        ris=[]

        query="""select distinct t.`year` as y
from teams t 
where t.`year` >= 1980"""

        cursor.execute(query)

        for row in cursor.fetchall():
            ris.append(row["y"])

        cursor.close()
        conn.close()

        return ris

    @staticmethod
    def getSquadreAnno(anno):

        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        ris = []

        query = """select t.ID, t.teamCode 
                    from teams t
                    where t.`year` = %s"""

        cursor.execute(query,(anno,))

        for row in cursor.fetchall():
            ris.append(Team(*row))

        cursor.close()
        conn.close()

        return ris