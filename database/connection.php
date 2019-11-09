<?php

   $m = new MongoDB\Driver\Manager("mongodb://localhost:27017");
	
   echo "Connection to database successfully";

   $db = $m->yash;
//    $data = $db->userdata;
//    $cursor = $data.find();
//    foreach($cursor as $document)
//    {
//        echo $document["full_name"]."\n";
//    }
	
   echo "Database mydb selected";
?>