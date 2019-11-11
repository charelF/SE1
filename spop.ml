(* 05.11.19 12:01 *)
(* Charel Felten *)
(* SPOP-Filesystem *)
(* small file system ... *)


exception ImpossibleAction of string


type file =
	| Directory of (string * file list)
	| TextFile of (string * string)
	| PythonFile of (string * string)


let combine f1 f2 = 
	match f1, f2 with
		| Directory(n, c), any -> Directory(n, any::c)
		| any, Directory(n, c) -> Directory(n, any::c)
		| TextFile(n1, c1), TextFile(n2, c2) -> TextFile(n1^"+"^n2, c1^"\n"^c2)
		| _, _ -> raise (ImpossibleAction "can not combine these kinds of files")

let print f =
	let rec aux f pre = 
		match f with
			| Directory(n, c) ->
				begin
				match c with
					| [Directory(_, _)] -> print_string pre
					| _ -> print_string "xxxx"
				end;
				
				print_string n;
				print_newline ();
				List.iter (fun i -> aux i (pre ^ "+---")) c
			| TextFile(n, _) -> print_string pre; print_string n; print_newline ()
			| PythonFile(n, _) -> print_string pre; print_string n; print_newline ()

	in aux f ""

	
(*************************  tests ********************************)

let charel = Directory("charel", [])

let sub1 = Directory("sub1", [])

let file1 = TextFile("txt1", "this is the content")

let file2 = PythonFile("py1", "this is python");;

let charel = combine charel sub1


let main = Directory("main", [charel; sub1; file1; file2]);;


print main;;









(* Sys.command "python3 -c 'a=2+2; print(a)'";; *)
