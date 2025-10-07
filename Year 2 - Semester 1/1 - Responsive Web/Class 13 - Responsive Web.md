---
tags:
  - incomplete
date: 2025-10-07
teacher: Mr. Oliver
---
# Responsive Web 5
## CSS Grid

```css
.gridContainer{
	display: grid;
	/* Gives gap to each items in the grid. */
	gap: 10px;
	
	/* Acceptable syntax: 1px 1fr */
	grid-template-rows: auto auto minmax(10px, 1fr);
	grid-template-columns: repeat(3, 1fr);
	
	/* Used to specify what items occupy what area.
	Requires grid-area: [item-name] */
	grid-template-areas:
		"box9 box7 box5"
		"box1 box2 box3"
		"box8 box6 box4";
	
	/* Default is stretch.
	Acceptable syntax: stretch, start, end, space-evenly, space-around */
	justify-items: start;
	align-items: start;
}

#item0{
	grid-column-start: 1;
	grid-column-end: 4;
	grid-row-start: 1;
	grid-row-end: 4;

	/* Shorthand notations */
	
	/* 
	grid-column: 1/4;
	grid-row: 1/4;
	grid-column: span 2;
	grid-row: span 2;
	*/
}

#item1{
	/* An even shorter hand notation used for covering an area of the grid.
	The sequence of numbers represent grid-row-start, grid-row-end, grid-column-start, and grid-column-end. */
	grid-area:
		1 / 1 /
		3 / 3;
}
```

----------------------------------------------------------------
# Editor's Notes