function solution(wallpaper) {
    var top = wallpaper.findIndex(w => w.includes('#'));
    var bottom = wallpaper.reduce((acc, curr, index) => curr.includes('#') ? index : acc, -1) + 1;
    var left = wallpaper.map(w => w.includes('#') ? w.indexOf('#') : 51).sort((a, b) => a - b).at(0);
    var right = wallpaper.map(w => w.includes('#') ? w.lastIndexOf('#') : 0).sort((a, b) => b - a).at(0) + 1;
    return [top, left, bottom, right];
}