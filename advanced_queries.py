import json

#best_fields
def multi_match_agg_best(query, fields=['artist_name','songs']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "genre.keyword",
					"size": 10
				}
			},
			"Gender Filter": {
				"terms": {
					"field": "gender.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_best(query, sort_num, fields=['artist_name','songs']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"votes": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "genre.keyword",
					"size": 10
				}
			},
			"Gender Filter": {
				"terms": {
					"field": "gender.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

#cross_fields
def multi_match_agg_cross(query, fields=['artist_name','songs']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "sinhala_genre.keyword",
					"size": 10
				}
			},
			"Gender Filter": {
				"terms": {
					"field": "gender.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_cross(query, sort_num, fields=['artist_name','songs']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"votes": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "genre.keyword",
					"size": 10
				}
			},
			"Gender Filter": {
				"terms": {
					"field": "gender.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q


#phrase_fields
def multi_match_agg_phrase(query, fields=['artist_name','songs']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "genre.keyword",
					"size": 10
				}
			},
			"Gender Filter": {
				"terms": {
					"field": "gender.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_phrase(query, sort_num, fields=['artist_name','songs']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"votes": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "genre.keyword",
					"size": 10
				}
			},
			"Gender Filter": {
				"terms": {
					"field": "gender.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

