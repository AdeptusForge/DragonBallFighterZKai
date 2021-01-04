--REORDER TRACK VIEW
--Version 2.0
--Started 08/20/1998 (version 1.0)
--Edited: 08/25/1999
--by Borislav Petrov
--http://gfxcentral.com/bobo/
-------------------------------------------------------


utility reorder_tv "Reorder TrackView"
(

group "About..."
(
label rtv01 "Reorder TrackView"
label rtv02 "Version 2.0 - 8/25/99"
label rtv03 "by Bobo's Rendert**ls"
label rtv04 "http://gfxcentral.com/bobo"
)
group "Reorder Selection"
(
button movetop "TOP" width:32 height:20 across:4 align:#left enabled:true
button moveup "UP" width:32 height:20 align:#center enabled:true 
button movedown "DN" width:32 height:20 align:#center enabled:true
button movebottom "END" width:32 height:20 align:#right enabled:true


radiobuttons single_mode "Up/Down Single Node" Labels:#("by Order","by Name") default:2 align:#center
)

group "Sort..."
(
button name_sort "TopLevel Nodes" width:140 enabled:true align:#center
button sub_sort "Children of Selected Nodes" width:140 enabled:true align:#center
radiobuttons descend_mode "" Labels:#("Ascend","Descend") default:1 align:#center
)

group "Sort Info"
(
label labelinfo01 ""
label labelinfo02 ""
label labelinfo03 "Ready."
)


on movetop pressed do
(

obj_array = $* as array
sel_array = selection as array
d = dummy ()
for i = 1 to obj_array.count do
(
if obj_array[i].parent == undefined then
	(
	move_it = true
	for j = 1 to sel_array.count do if obj_array[i] == sel_array[j] then move_it = false
			if move_it then
			(
			obj_array[i].parent = d
			obj_array[i].parent = undefined
			)
	)
)--end i loop
delete d
)--end movetop


on movebottom pressed do
(
sel_array = selection as array
for j = 1 to sel_array.count do
	(
	if sel_array[j].parent == undefined then
		(
		d = dummy ()
		sel_array[j].parent = d
		delete d
		)
	)--end j loop	
)--end movebottom


on moveup pressed do
(
sel_array = #()
obj_array = $* as array
sel_array = for nodes in selection collect nodes.name
if single_mode.state == 2 then sort sel_array

	list_array = #()
	current_pos = 0
	for i = 1 to obj_array.count do 
	(
	if obj_array[i].parent == undefined then append list_array obj_array[i]
	if obj_array[i].name == sel_array[1] then current_pos = list_array.count
	)
	
	if current_pos >1 then
	(
	d = dummy ()
	list_array[current_pos-1].parent = d
	list_array[current_pos].parent = d
	delete d
	d = dummy ()
	for i = list_array.count to current_pos+1 by -1 do
	(
	list_array[i].parent = d
	)
	delete d
	)--end if
)--end moveup


on movedown pressed do
(
obj_array = #()
sel_array = #()
current_pos = 0
sel_array = for nodes in selection collect nodes.name
if single_mode.state == 2 then sort sel_array
obj_array = for object in $* collect object

list_array = #()
for i = 1 to obj_array.count do 
(
if obj_array[i].parent == undefined then append list_array obj_array[i]
if obj_array[i].name == sel_array[1] then current_pos = list_array.count
)
if current_pos <list_array.count and current_pos != 0 then
(
d = dummy ()
list_array[current_pos].parent = d
list_array[current_pos+1].parent = d


delete d
d = dummy ()
for i = list_array.count to current_pos+2 by -1 do
(
	list_array[i].parent = d
)
delete d
)--end if

)--end movedown



on name_sort pressed do
(
user_break = false
obj_array = #()
sort_array = #()
obj_old_names = #()
obj_array = for object in $* collect object 
labelinfo03.text = "Sorting by Name..."
start_time = timestamp()
for i = 1 to obj_array.count do
(
if obj_array[i].parent == undefined then 
		(
		append sort_array ("'"+obj_array[i].name+"'")
		)
)
txt = "TopNodes In Scene:" + sort_array.count as string
labelinfo01.text = txt

sort sort_array
name_array = #()

if descend_mode.state == 2 then
(
start_v = 1
end_v = sort_array.count 
step_v = 1
)
else
(
start_v = sort_array.count 
end_v = 1
step_v = -1
)

progressstart "Sorting TrackView..."
progressupdate (1)

d = point ()
for i = start_v to end_v by step_v do
(


if descend_mode.state == 2 then 
	(
	progress_percent = ((i) as float / (end_v)as float) * 100
	)
	else
	(
	progress_percent = ((start_v-i) as float / (start_v)as float) * 100
	)
	
	if not progressupdate(progress_percent) then user_break = true
	if user_break then exit

sort_node = execute ("$"+sort_array[i])
index_found = finditem obj_array sort_node

if index_found != undefined and obj_array[index_found].parent == undefined then obj_array[index_found].parent = d
)
delete d

end_time = timestamp()
progressend ()
total_time = (end_time-start_time) as float / 1000.0
txt = "Last Sort Time: " + total_time as string + "s"
labelinfo02.text = txt
if user_break then labelinfo03.text = "Canceled." else labelinfo03.text = "Ready."

)--end name_sort



on sub_sort pressed do
(
user_break = false
obj_array = #()
child_array = #()
kids_array =#()
sort_array = #()
obj_array = for object in selection collect object 
labelinfo03.text = "Sorting Children by Name..."
start_time = timestamp()
txt = "Selected Nodes:" + obj_array.count as string
labelinfo01.text = txt

for n = 1 to obj_array.count do
(
child_array = obj_array[n].children
for j = 1 to child_array.count do 
	(
	append kids_array child_array[j]
	)

for i = 1 to kids_array.count do
	(
	append sort_array ("'"+kids_array[i].name+"'")
	)


sort sort_array
name_array = #()

if descend_mode.state == 1 then
(
start_v = 1
end_v = sort_array.count 
step_v = 1
)
else
(
start_v = sort_array.count 
end_v = 1
step_v = -1
)
user_break = false
		progressstart "Sorting Children..."
		progressupdate (1)

for i = start_v to end_v by step_v do
(
progress_percent = ((i) as float / (sort_array.count)as float) * 100
	if not progressupdate(progress_percent) then user_break = true
	if user_break then exit	

sort_node = execute ("$"+sort_array[i])
index_found = finditem kids_array sort_node
if kids_array[index_found] != undefined then
(
old_parent = kids_array[index_found].parent 
kids_array[index_found].parent = undefined
kids_array[index_found].parent = old_parent
)
)--end i loop

)--end n loop

end_time = timestamp()
progressend ()
total_time = (end_time-start_time) as float / 1000.0
txt = "Last Sort Time: " + total_time as string + "s"
labelinfo02.text = txt
if user_break then labelinfo03.text = "Canceled." else labelinfo03.text = "Ready."

)--end sub_sort


)--end util