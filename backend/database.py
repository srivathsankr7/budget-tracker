from cassandra.cluster import Cluster


def create_session():
    cluster = Cluster()
    session = cluster.connect('budgettracker')
    return session
