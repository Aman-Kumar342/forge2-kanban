<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
class Tag extends Model {
    protected $fillable = ['board_id', 'name', 'color'];
    public function board(): BelongsTo { return $this->belongsTo(Board::class); }
}
