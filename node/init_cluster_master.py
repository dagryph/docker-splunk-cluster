import os

import init_helpers


def configurations():
    return {
        "components": {
            "kvstore": False,
            "web": True,
            "indexing": False
        }
    }


def substitution():
    return {
        "@CLUSTERING_PASS_4_SYMM_KEY@": "example_cluster_secret",
        "@CLUSTERING_REPLICATION_FACTOR@": "1",
        "@CLUSTERING_SEARCH_FACTOR@": "1",
        "@INDEX_DISCOVERY_PASS_4_SYMM_KEY@": "example_index_discovery_secret",
        "@SHCLUSTERING_PASS_4_SYMM_KEY@": "example_shc_secret"
    }
