e_id = 1

txt = ""
txt += "select"
txt += "*from emp"


txt1 = """
select *
from emp
where e_id ='{}'
""".format(e_id)

print(txt1)


txt2 = f"""
select *
from emp
where e_id ='{e_id}'
"""

print(txt2)

