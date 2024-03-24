<<<<<<< HEAD
/**
 *
 * @param json The json read from directus. Currently read from data base but can be converted easily.
 * @returns: rowMapPrice -> Returns the all materials into an array
 */
export default function JsonToAtom(json: any[]): any[] {
  let array: any[] = [];
  for (let i: number = 0; i < json.length; i++) {
    const changeToNumber: number = Number(json[i].price);
    /** 
    array.push(
      createRowPrice(
        json[i].material,
        json[i].material,
        json[i].formula,
        i.toString(),
        json[i].supplier ? json[i].supplier : "-",
        changeToNumber
      )
    );
    */
  }
  return array;
}
=======
/**
 *
 * @param json The json read from directus. Currently read from data base but can be converted easily.
 * @returns: rowMapPrice -> Returns the all materials into an array
 */
export default function JsonToAtom(json: any[]): any[] {
  let array: any[] = [];
  for (let i: number = 0; i < json.length; i++) {
    const changeToNumber: number = Number(json[i].price);
    /** 
    array.push(
      createRowPrice(
        json[i].material,
        json[i].material,
        json[i].formula,
        i.toString(),
        json[i].supplier ? json[i].supplier : "-",
        changeToNumber
      )
    );
    */
  }
  return array;
}
>>>>>>> main
