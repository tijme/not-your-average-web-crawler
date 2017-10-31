<!DOCTYPE html>
<html>
    <body>
        <?php
            $depth = 10000;
            $current = isset($_GET['depth']) ? (int) $_GET['depth'] : 0;

            $from = $current <= $depth && $current >= 0 ? $current : 0;
            $to = $from + 100 <= $depth && $from >= 0 ? $from + 100 : $depth;

            for ($i = $from; $i <= $to; $i ++) {
                echo '<a href="?depth=' . $i . '">Depth: ' . $i . '</a><br>';
            }
        ?>
    </body>
</html>