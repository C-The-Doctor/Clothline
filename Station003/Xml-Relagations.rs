use std::fs::File;
use simple_xml_builder::XMLElement;


let parser = xml::reader::EventReader::new(file);
for event in parser {
    println!("{:?}", event.unwrap());
}



#[derive(Debug, Deserialize)]
struct Document {
    param: Option<String>,
    first_element: String,
    second_element: SecondElement,
}

let doc: Document = quick_xml::de::from_str(xml).unwrap();


struct Document {
    records: Vec<Result<Record, Error>>
}
