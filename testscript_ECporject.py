import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECproject.settings')

import django
django.setup()

from User.models import Subject, UserProfile


def testscript():

    add_cat="10"
    add_page(uid=add_cat, uname="xiaoming",passwd="123",sex="1", rname="hehe", rdate="1990-05-06", pro="bei", town="jing", area="he", adds="vvvvv")

    add_cat="20"
    add_page(uid=add_cat, uname="daming",passwd="123",sex="0", rname="haha", rdate="1994-02-13", pro="nan", town="jing", area="ha", adds="bbbbb")

    # Print out what we have added to the user.
    for c in Subject.objects.all():
        for p in Subject.objects.filter(Subject=c):
            print "- {0} - {1}".format(str(c), str(p))

# def this
def add_page(uid, uname, passwd, sex, rname, rdate, pro, town, area, adds):
    p = Subject.objects.get_or_create(user_id=uid, user_name=uname, user_passwd=passwd, sex=sex, real_name=rname, register_date=rdate, province=pro, town=town, area=area, address=adds)[0]
    return p

def add_cat(uid):
    c = Subject.objects.get_or_create(uid=uid)[0]
    return c

# now begin!
if __name__ == '__main__':
    print "Starting itcastsubject population script..."
    testscript()
