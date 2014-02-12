from db_connection_helpers import get_db_connection

def insert_data_portal_record(form_data):
  conn = get_db_connection()
  db = conn.cursor()
  data_set_array = [form_data.get("Field" + str(x)) for x in range(4, 16) 
                    if form_data.get("Field" + str(x)) is not None]
  data_sets = ', '.join(data_set_array)
  included_formats_array = [form_data.get("Field" + str(x)) for x in range(105, 109) 
                    if form_data.get("Field" + str(x)) is not None]
  included_formats = ','.join(included_formats_array)                    
  insert_statement = db.mogrify("""insert into data_portals (place, portal_url, data_sets, 
                                included_formats, press_release_url, data_completeness, comments) 
                                values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % \
                                (form_data['Field1'], form_data["Field2"], data_sets, 
                                 included_formats, form_data["Field209"], form_data["Field205"],
                                 form_data["Field207"]))
  db.execute(insert_statement)
  conn.commit()
  conn.close()
  